const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".nav");
const navLinks = [...document.querySelectorAll(".nav a[data-section]")];
const sections = navLinks
  .map((link) => document.getElementById(link.dataset.section))
  .filter(Boolean);

function closeMenu() {
  nav?.classList.remove("is-open");
  toggle?.setAttribute("aria-expanded", "false");
}

toggle?.addEventListener("click", () => {
  const open = nav.classList.toggle("is-open");
  toggle.setAttribute("aria-expanded", String(open));
});

navLinks.forEach((link) => link.addEventListener("click", closeMenu));

function updateActiveNav(updateUrl = false) {
  if (!sections.length) return;

  const marker = window.scrollY + 79;
  let current = sections[0];

  for (const section of sections) {
    if (section.offsetTop <= marker) current = section;
  }

  navLinks.forEach((link) => {
    const active = link.dataset.section === current.id;
    link.classList.toggle("is-active", active);
    if (active) link.setAttribute("aria-current", "page");
    else link.removeAttribute("aria-current");
  });

  // Keep the address bar in sync while scrolling (no extra history entries)
  if (updateUrl) {
    const atTop = window.scrollY < 40;
    const hash = atTop ? "" : "#" + current.id;
    if (location.hash !== hash) {
      history.replaceState(
        null,
        "",
        location.pathname + location.search + hash,
      );
    }
  }
}

window.addEventListener("scroll", () => updateActiveNav(true), {
  passive: true,
});
window.addEventListener("resize", () => updateActiveNav());

updateActiveNav();
