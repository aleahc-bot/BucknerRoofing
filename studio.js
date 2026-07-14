/* ============================================================
   BUCKNER ROOFING — studio.js
   Design Studio + nav + reveal + gallery filter.
   Preferences persist across pages via localStorage (guarded).
   ============================================================ */
(function () {
  "use strict";

  var AXES = {
    layout: ["crest", "split", "fixbild", "roofguard", "ridge"],
    type: ["contemporary", "luxury"],
    theme: ["light", "dark"],
    scale: ["spacious", "compact"]
  };
  var DEFAULTS = { layout: "crest", type: "contemporary", theme: "light", scale: "spacious" };
  var KEY = "buckner.studio.v2";
  var root = document.documentElement;

  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      if (!raw) return Object.assign({}, DEFAULTS);
      var saved = JSON.parse(raw);
      var out = Object.assign({}, DEFAULTS);
      Object.keys(AXES).forEach(function (k) {
        if (AXES[k].indexOf(saved[k]) > -1) out[k] = saved[k];
      });
      return out;
    } catch (e) {
      return Object.assign({}, DEFAULTS);
    }
  }

  function save(state) {
    try { window.localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) { /* private mode: session only */ }
  }

  var state = load();

  function apply(state) {
    Object.keys(AXES).forEach(function (k) { root.setAttribute("data-" + k, state[k]); });
    document.querySelectorAll("[data-axis]").forEach(function (btn) {
      var on = state[btn.dataset.axis] === btn.dataset.value;
      btn.classList.toggle("is-on", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
    document.querySelectorAll("[data-readout]").forEach(function (el) {
      var v = state[el.dataset.readout];
      el.textContent = v.charAt(0).toUpperCase() + v.slice(1);
    });
  }

  /* paint the saved state before first paint to avoid a flash */
  apply(state);

  document.addEventListener("DOMContentLoaded", function () {
    apply(state);

    /* ---- Design Studio ---- */
    var fab = document.getElementById("studioFab");
    var drawer = document.getElementById("studio");
    var veil = document.getElementById("studioVeil");

    function openStudio() {
      document.body.classList.add("studio-open");
      if (drawer) drawer.setAttribute("aria-hidden", "false");
      if (fab) fab.setAttribute("aria-expanded", "true");
    }
    function closeStudio() {
      document.body.classList.remove("studio-open");
      if (drawer) drawer.setAttribute("aria-hidden", "true");
      if (fab) fab.setAttribute("aria-expanded", "false");
    }

    if (fab) fab.addEventListener("click", function () {
      document.body.classList.contains("studio-open") ? closeStudio() : openStudio();
    });
    if (veil) veil.addEventListener("click", closeStudio);
    var xBtn = document.getElementById("studioClose");
    if (xBtn) xBtn.addEventListener("click", closeStudio);

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeStudio(); document.body.classList.remove("menu-open"); }
    });

    document.querySelectorAll("[data-axis]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        state[btn.dataset.axis] = btn.dataset.value;
        save(state);
        apply(state);
      });
    });

    var reset = document.getElementById("studioReset");
    if (reset) reset.addEventListener("click", function () {
      state = Object.assign({}, DEFAULTS);
      save(state);
      apply(state);
    });

    /* ---- sticky nav ---- */
    var nav = document.querySelector(".nav");
    var hero = document.querySelector(".hero");
    function onScroll() {
      if (!nav) return;
      /* Inner pages have no hero, so the nav never floats over a photo.
         It sits solid from the first pixel. */
      if (!hero) {
        nav.classList.add("is-stuck");
        nav.classList.remove("nav--over");
        return;
      }
      var stuck = window.scrollY > Math.min(hero.offsetHeight - 90, 220);
      nav.classList.toggle("is-stuck", stuck);
      nav.classList.toggle("nav--over", !stuck);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });

    /* ---- mobile menu ---- */
    var burger = document.getElementById("burger");
    if (burger) burger.addEventListener("click", function () {
      document.body.classList.toggle("menu-open");
    });
    document.querySelectorAll(".nav__links a").forEach(function (a) {
      a.addEventListener("click", function () { document.body.classList.remove("menu-open"); });
    });

    /* ---- scroll reveal ---- */
    var items = document.querySelectorAll(".rv");
    if (!window.IntersectionObserver || window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      items.forEach(function (el) { el.classList.add("in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry, i) {
          if (entry.isIntersecting) {
            var el = entry.target;
            setTimeout(function () { el.classList.add("in"); }, i * 70);
            io.unobserve(el);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -60px 0px" });
      items.forEach(function (el) { io.observe(el); });
    }

    /* ---- gallery filter ---- */
    var filterBtns = document.querySelectorAll("[data-filter]");
    filterBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var cat = btn.dataset.filter;
        filterBtns.forEach(function (b) { b.classList.toggle("is-on", b === btn); });
        document.querySelectorAll("[data-cat]").forEach(function (card) {
          card.classList.toggle("is-hidden", cat !== "all" && card.dataset.cat !== cat);
        });
      });
    });

    /* ---- quote form (front-end only; wire to GHL / Formspree on deploy) ---- */
    var form = document.getElementById("quoteForm");
    if (form) form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("formNote");
      if (note) note.textContent = "Thanks. Your request is ready to send — connect this form to your CRM to go live.";
      form.reset();
    });
  });
})();
