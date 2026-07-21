/* ============================================================
   BUCKNER ROOFING — site.js
   Sticky nav, mobile menu, scroll reveal, gallery filter, quote form.
   The Design Studio has been removed; the design is locked in index.css.
   ============================================================ */
(function () {
  "use strict";

  document.addEventListener("DOMContentLoaded", function () {

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
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") document.body.classList.remove("menu-open");
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

    /* ---- dev tool: point the preview launcher at the CURRENT page ---- */
    var devbtn = document.querySelector(".devbtn");
    if (devbtn) {
      var here = window.location.pathname.split("/").pop() || "index.html";
      devbtn.href = "preview.html?p=" + encodeURIComponent(here);
    }

    /* ---- testimonial carousel ---- */
    var track = document.getElementById("quotes");
    if (track) {
      var prev = document.querySelector(".qnav--prev");
      var next = document.querySelector(".qnav--next");
      function step() {
        var first = track.querySelector(".quote");
        if (!first) return track.clientWidth;
        var gap = parseFloat(getComputedStyle(track).columnGap) || 0;
        return first.getBoundingClientRect().width + gap;
      }
      function sync() {
        var max = track.scrollWidth - track.clientWidth - 2;
        if (prev) prev.disabled = track.scrollLeft <= 2;
        if (next) next.disabled = track.scrollLeft >= max;
      }
      if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
      if (next) next.addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });
      track.addEventListener("scroll", sync, { passive: true });
      window.addEventListener("resize", sync);
      sync();
    }

    /* ---- quote form (front-end only; wire to GHL / Formspree on deploy) ---- */
    var form = document.getElementById("quoteForm");
    if (form) form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = document.getElementById("formNote");
      if (note) note.textContent = "Thanks. Your request is ready to send \u2014 connect this form to your CRM to go live.";
      form.reset();
    });
  });
})();
