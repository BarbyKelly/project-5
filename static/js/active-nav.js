// jshint esversion: 6
// Navbar adjustments and active-nav.js created with guidance from ChatGPT


document.addEventListener("DOMContentLoaded", () => {
    const presentPath = window.location.pathname.replace(/\/$/, "");
    const searchParams = new URLSearchParams(window.location.search);

    const navLinks = document.querySelectorAll(".navbar-nav .nav-link, .navbar-nav .dropdown-item");

    navLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (!href || href === "#") return;

        // Split into pathname and query string
        const [linkPath, linkQuery] = href.split("?");
        const pathOnly = linkPath.replace(/\/$/, "");

        // Compare pathnames
        if (presentPath === pathOnly) {
            // If the link has query parameters, check if they match the current URL
            if (linkQuery) {
                const linkParams = new URLSearchParams(linkQuery);
                let match = true;
                for (const [key, value] of linkParams.entries()) {
                    if (searchParams.get(key) !== value) {
                        match = false;
                        break;
                    }
                }
                if (!match) return;
            }

            // Mark link as active
            link.classList.add("active");

            // If the link is in dropdown menu, mark parent active too
            const parent = link.closest(".dropdown");
            if (parent) {
                const parentLink = parent.querySelector(".nav-link.dropdown-toggle");
                if (parentLink) parentLink.classList.add("active");
            }
        }
    });
});
