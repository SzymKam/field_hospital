/*!
 * Time picker for pickadate.js v3.5.6
 * http://amsul.github.io/pickadate.js/time.htm
 */
!(function (a) {
  "function" == typeof define && define.amd
    ? define(["picker", "jquery"], a)
    : "object" == typeof exports
    ? (module.exports = a(require("./picker.js"), require("jquery")))
    : a(Picker, jQuery);
})(function (a, b) {
  function c(a, b) {
    var c = this,
      d = a.$node[0].value,
      e = a.$node.data("value"),
      f = e || d,
      g = e ? b.formatSubmit : b.format;
    (c.settings = b),
      (c.$node = a.$node),
      (c.queue = {
        interval: "i",
        min: "measure create",
        max: "measure create",
        now: "now create",
        select: "parse create validate",
        highlight: "parse create validate",
        view: "parse create validate",
        disable: "deactivate",
        enable: "activate",
      }),
      (c.item = {}),
      (c.item.clear = null),
      (c.item.interval = b.interval || 30),
      (c.item.disable = (b.disable || []).slice(0)),
      (c.item.enable = -(function (a) {
        return a[0] === !0 ? a.shift() : -1;
      })(c.item.disable)),
      c.set("min", b.min).set("max", b.max).set("now"),
      f
        ? c.set("select", f, { format: g })
        : c.set("select", null).set("highlight", c.item.now),
      (c.key = {
        40: 1,
        38: -1,
        39: 1,
        37: -1,
        go: function (a) {
          c.set("highlight", c.item.highlight.pick + a * c.item.interval, {
            interval: a * c.item.interval,
          }),
            this.render();
        },
      }),
      a
        .on(
          "render",
          function () {
            var c = a.$root.children(),
              d = c.find("." + b.klass.viewset),
              e = function (a) {
                return ["webkit", "moz", "ms", "o", ""].map(function (b) {
                  return (b ? "-" + b + "-" : "") + a;
                });
              },
              f = function (a, b) {
                e("transform").map(function (c) {
                  a.css(c, b);
                }),
                  e("transition").map(function (c) {
                    a.css(c, b);
                  });
              };
            d.length &&
              (f(c, "none"),
              (c[0].scrollTop = ~~d.position().top - 2 * d[0].clientHeight),
              f(c, ""));
          },
          1,
        )
        .on(
          "open",
          function () {
            a.$root.find("button").attr("disabled", !1);
          },
          1,
        )
        .on(
          "close",
          function () {
            a.$root.find("button").attr("disabled", !0);
          },
          1,
        );
  }
  var d = 24,
    e = 60,
    f = 12,
    g = d * e,
    h = a._;
  (c.prototype.set = function (a, b, c) {
    var d = this,
      e = d.item;
    return null === b
      ? ("clear" == a && (a = "select"), (e[a] = b), d)
      : ((e["enable" == a ? "disable" : "flip" == a ? "enable" : a] = d.queue[a]
          .split(" ")
          .map(function (e) {
            return (b = d[e](a, b, c));
          })
          .pop()),
        "select" == a
          ? d.set("highlight", e.select, c)
          : "highlight" == a
          ? d.set("view", e.highlight, c)
          : "interval" == a
          ? d.set("min", e.min, c).set("max", e.max, c)
          : a.match(/^(flip|min|max|disable|enable)$/) &&
            (e.select && d.disabled(e.select) && d.set("select", b, c),
            e.highlight && d.disabled(e.highlight) && d.set("highlight", b, c),
            "min" == a && d.set("max", e.max, c)),
        d);
  }),
    (c.prototype.get = function (a) {
      return this.item[a];
    }),
    (c.prototype.create = function (a, c, f) {
      var i = this;
      return (
        (c = void 0 === c ? a : c),
        h.isDate(c) && (c = [c.getHours(), c.getMinutes()]),
        b.isPlainObject(c) && h.isInteger(c.pick)
          ? (c = c.pick)
          : b.isArray(c)
          ? (c = +c[0] * e + +c[1])
          : h.isInteger(c) || (c = i.now(a, c, f)),
        "max" == a && c < i.item.min.pick && (c += g),
        "min" != a &&
          "max" != a &&
          (c - i.item.min.pick) % i.item.interval !== 0 &&
          (c += i.item.interval),
        (c = i.normalize(a, c, f)),
        {
          hour: ~~(d + c / e) % d,
          mins: (e + (c % e)) % e,
          time: (g + c) % g,
          pick: c % g,
        }
      );
    }),
    (c.prototype.createRange = function (a, c) {
      var d = this,
        e = function (a) {
          return a === !0 || b.isArray(a) || h.isDate(a) ? d.create(a) : a;
        };
      return (
        h.isInteger(a) || (a = e(a)),
        h.isInteger(c) || (c = e(c)),
        h.isInteger(a) && b.isPlainObject(c)
          ? (a = [c.hour, c.mins + a * d.settings.interval])
          : h.isInteger(c) &&
            b.isPlainObject(a) &&
            (c = [a.hour, a.mins + c * d.settings.interval]),
        { from: e(a), to: e(c) }
      );
    }),
    (c.prototype.withinRange = function (a, b) {
      return (
        (a = this.createRange(a.from, a.to)),
        b.pick >= a.from.pick && b.pick <= a.to.pick
      );
    }),
    (c.prototype.overlapRanges = function (a, b) {
      var c = this;
      return (
        (a = c.createRange(a.from, a.to)),
        (b = c.createRange(b.from, b.to)),
        c.withinRange(a, b.from) ||
          c.withinRange(a, b.to) ||
          c.withinRange(b, a.from) ||
          c.withinRange(b, a.to)
      );
    }),
    (c.prototype.now = function (a, b) {
      var c,
        d = this.item.interval,
        f = new Date(),
        g = f.getHours() * e + f.getMinutes(),
        i = h.isInteger(b);
      return (
        (g -= g % d),
        (c = 0 > b && -d >= d * b + g),
        (g += "min" == a && c ? 0 : d),
        i && (g += d * (c && "max" != a ? b + 1 : b)),
        g
      );
    }),
    (c.prototype.normalize = function (a, b) {
      var c = this.item.interval,
        d = (this.item.min && this.item.min.pick) || 0;
      return (b -= "min" == a ? 0 : (b - d) % c);
    }),
    (c.prototype.measure = function (a, c, f) {
      var g = this;
      return (
        c || (c = "min" == a ? [0, 0] : [d - 1, e - 1]),
        "string" == typeof c
          ? (c = g.parse(a, c))
          : c === !0 || h.isInteger(c)
          ? (c = g.now(a, c, f))
          : b.isPlainObject(c) &&
            h.isInteger(c.pick) &&
            (c = g.normalize(a, c.pick, f)),
        c
      );
    }),
    (c.prototype.validate = function (a, b, c) {
      var d = this,
        e = c && c.interval ? c.interval : d.item.interval;
      return (
        d.disabled(b) && (b = d.shift(b, e)),
        (b = d.scope(b)),
        d.disabled(b) && (b = d.shift(b, -1 * e)),
        b
      );
    }),
    (c.prototype.disabled = function (a) {
      var c = this,
        d = c.item.disable.filter(function (d) {
          return h.isInteger(d)
            ? a.hour == d
            : b.isArray(d) || h.isDate(d)
            ? a.pick == c.create(d).pick
            : b.isPlainObject(d)
            ? c.withinRange(d, a)
            : void 0;
        });
      return (
        (d =
          d.length &&
          !d.filter(function (a) {
            return (
              (b.isArray(a) && "inverted" == a[2]) ||
              (b.isPlainObject(a) && a.inverted)
            );
          }).length),
        -1 === c.item.enable
          ? !d
          : d || a.pick < c.item.min.pick || a.pick > c.item.max.pick
      );
    }),
    (c.prototype.shift = function (a, b) {
      var c = this,
        d = c.item.min.pick,
        e = c.item.max.pick;
      for (
        b = b || c.item.interval;
        c.disabled(a) &&
        ((a = c.create((a.pick += b))), !(a.pick <= d || a.pick >= e));

      );
      return a;
    }),
    (c.prototype.scope = function (a) {
      var b = this.item.min.pick,
        c = this.item.max.pick;
      return this.create(a.pick > c ? c : a.pick < b ? b : a);
    }),
    (c.prototype.parse = function (a, b, c) {
      var d,
        f,
        g,
        i,
        j,
        k = this,
        l = {};
      if (!b || "string" != typeof b) return b;
      (c && c.format) || ((c = c || {}), (c.format = k.settings.format)),
        k.formats.toArray(c.format).map(function (a) {
          var c,
            d = k.formats[a],
            e = d ? h.trigger(d, k, [b, l]) : a.replace(/^!/, "").length;
          d && ((c = b.substr(0, e)), (l[a] = c.match(/^\d+$/) ? +c : c)),
            (b = b.substr(e));
        });
      for (i in l)
        (j = l[i]),
          h.isInteger(j)
            ? i.match(/^(h|hh)$/i)
              ? ((d = j), ("h" == i || "hh" == i) && (d %= 12))
              : "i" == i && (f = j)
            : i.match(/^a$/i) &&
              j.match(/^p/i) &&
              ("h" in l || "hh" in l) &&
              (g = !0);
      return (g ? d + 12 : d) * e + f;
    }),
    (c.prototype.formats = {
      h: function (a, b) {
        return a ? h.digits(a) : b.hour % f || f;
      },
      hh: function (a, b) {
        return a ? 2 : h.lead(b.hour % f || f);
      },
      H: function (a, b) {
        return a ? h.digits(a) : "" + (b.hour % 24);
      },
      HH: function (a, b) {
        return a ? h.digits(a) : h.lead(b.hour % 24);
      },
      i: function (a, b) {
        return a ? 2 : h.lead(b.mins);
      },
      a: function (a, b) {
        return a ? 4 : g / 2 > b.time % g ? "a.m." : "p.m.";
      },
      A: function (a, b) {
        return a ? 2 : g / 2 > b.time % g ? "AM" : "PM";
      },
      toArray: function (a) {
        return a.split(/(h{1,2}|H{1,2}|i|a|A|!.)/g);
      },
      toString: function (a, b) {
        var c = this;
        return c.formats
          .toArray(a)
          .map(function (a) {
            return h.trigger(c.formats[a], c, [0, b]) || a.replace(/^!/, "");
          })
          .join("");
      },
    }),
    (c.prototype.isTimeExact = function (a, c) {
      var d = this;
      return (h.isInteger(a) && h.isInteger(c)) ||
        ("boolean" == typeof a && "boolean" == typeof c)
        ? a === c
        : (h.isDate(a) || b.isArray(a)) && (h.isDate(c) || b.isArray(c))
        ? d.create(a).pick === d.create(c).pick
        : b.isPlainObject(a) && b.isPlainObject(c)
        ? d.isTimeExact(a.from, c.from) && d.isTimeExact(a.to, c.to)
        : !1;
    }),
    (c.prototype.isTimeOverlap = function (a, c) {
      var d = this;
      return h.isInteger(a) && (h.isDate(c) || b.isArray(c))
        ? a === d.create(c).hour
        : h.isInteger(c) && (h.isDate(a) || b.isArray(a))
        ? c === d.create(a).hour
        : b.isPlainObject(a) && b.isPlainObject(c)
        ? d.overlapRanges(a, c)
        : !1;
    }),
    (c.prototype.flipEnable = function (a) {
      var b = this.item;
      b.enable = a || (-1 == b.enable ? 1 : -1);
    }),
    (c.prototype.deactivate = function (a, c) {
      var d = this,
        e = d.item.disable.slice(0);
      return (
        "flip" == c
          ? d.flipEnable()
          : c === !1
          ? (d.flipEnable(1), (e = []))
          : c === !0
          ? (d.flipEnable(-1), (e = []))
          : c.map(function (a) {
              for (var c, f = 0; f < e.length; f += 1)
                if (d.isTimeExact(a, e[f])) {
                  c = !0;
                  break;
                }
              c ||
                ((h.isInteger(a) ||
                  h.isDate(a) ||
                  b.isArray(a) ||
                  (b.isPlainObject(a) && a.from && a.to)) &&
                  e.push(a));
            }),
        e
      );
    }),
    (c.prototype.activate = function (a, c) {
      var d = this,
        e = d.item.disable,
        f = e.length;
      return (
        "flip" == c
          ? d.flipEnable()
          : c === !0
          ? (d.flipEnable(1), (e = []))
          : c === !1
          ? (d.flipEnable(-1), (e = []))
          : c.map(function (a) {
              var c, g, i, j;
              for (i = 0; f > i; i += 1) {
                if (((g = e[i]), d.isTimeExact(g, a))) {
                  (c = e[i] = null), (j = !0);
                  break;
                }
                if (d.isTimeOverlap(g, a)) {
                  b.isPlainObject(a)
                    ? ((a.inverted = !0), (c = a))
                    : b.isArray(a)
                    ? ((c = a), c[2] || c.push("inverted"))
                    : h.isDate(a) &&
                      (c = [
                        a.getFullYear(),
                        a.getMonth(),
                        a.getDate(),
                        "inverted",
                      ]);
                  break;
                }
              }
              if (c)
                for (i = 0; f > i; i += 1)
                  if (d.isTimeExact(e[i], a)) {
                    e[i] = null;
                    break;
                  }
              if (j)
                for (i = 0; f > i; i += 1)
                  if (d.isTimeOverlap(e[i], a)) {
                    e[i] = null;
                    break;
                  }
              c && e.push(c);
            }),
        e.filter(function (a) {
          return null != a;
        })
      );
    }),
    (c.prototype.i = function (a, b) {
      return h.isInteger(b) && b > 0 ? b : this.item.interval;
    }),
    (c.prototype.nodes = function (a) {
      var b = this,
        c = b.settings,
        d = b.item.select,
        e = b.item.highlight,
        f = b.item.view,
        g = b.item.disable;
      return h.node(
        "ul",
        h.group({
          min: b.item.min.pick,
          max: b.item.max.pick,
          i: b.item.interval,
          node: "li",
          item: function (a) {
            a = b.create(a);
            var i = a.pick,
              j = d && d.pick == i,
              k = e && e.pick == i,
              l = g && b.disabled(a),
              m = h.trigger(b.formats.toString, b, [c.format, a]);
            return [
              h.trigger(b.formats.toString, b, [
                h.trigger(c.formatLabel, b, [a]) || c.format,
                a,
              ]),
              (function (a) {
                return (
                  j && a.push(c.klass.selected),
                  k && a.push(c.klass.highlighted),
                  f && f.pick == i && a.push(c.klass.viewset),
                  l && a.push(c.klass.disabled),
                  a.join(" ")
                );
              })([c.klass.listItem]),
              "data-pick=" +
                a.pick +
                " " +
                h.ariaAttr({
                  role: "option",
                  label: m,
                  selected: j && b.$node.val() === m ? !0 : null,
                  activedescendant: k ? !0 : null,
                  disabled: l ? !0 : null,
                }),
            ];
          },
        }) +
          h.node(
            "li",
            h.node(
              "button",
              c.clear,
              c.klass.buttonClear,
              "type=button data-clear=1" +
                (a ? "" : " disabled") +
                " " +
                h.ariaAttr({ controls: b.$node[0].id }),
            ),
            "",
            h.ariaAttr({ role: "presentation" }),
          ),
        c.klass.list,
        h.ariaAttr({ role: "listbox", controls: b.$node[0].id }),
      );
    }),
    (c.defaults = (function (a) {
      return {
        clear: "Clear",
        format: "h:i A",
        interval: 30,
        closeOnSelect: !0,
        closeOnClear: !0,
        klass: {
          picker: a + " " + a + "--time",
          holder: a + "__holder",
          list: a + "__list",
          listItem: a + "__list-item",
          disabled: a + "__list-item--disabled",
          selected: a + "__list-item--selected",
          highlighted: a + "__list-item--highlighted",
          viewset: a + "__list-item--viewset",
          now: a + "__list-item--now",
          buttonClear: a + "__button--clear",
        },
      };
    })(a.klasses().picker)),
    a.extend("pickatime", c);
});
