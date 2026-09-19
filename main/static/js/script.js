document.addEventListener("DOMContentLoaded", function () {
    const nav = document.querySelector(".site-navbar");
    const contactForm = document.getElementById("contact-form");

    function updateNavShadow() {
        if (!nav) {
            return;
        }
        if (window.scrollY > 8) {
            nav.style.boxShadow = "0 10px 24px rgba(0, 0, 0, 0.18)";
        } else {
            nav.style.boxShadow = "none";
        }
    }

    updateNavShadow();
    window.addEventListener("scroll", updateNavShadow);

    if (contactForm) {
        contactForm.addEventListener("submit", function (event) {
            const name = contactForm.querySelector("[name='name']");
            const email = contactForm.querySelector("[name='email']");
            const subject = contactForm.querySelector("[name='subject']");
            const message = contactForm.querySelector("[name='message']");
            const errors = [];

            if (!name.value.trim() || name.value.trim().length < 2) {
                errors.push("Please enter your name.");
            }
            if (!email.value.trim() || !email.value.includes("@")) {
                errors.push("Please enter a valid email address.");
            }
            if (!subject.value.trim() || subject.value.trim().length < 4) {
                errors.push("Please enter a subject.");
            }
            if (!message.value.trim() || message.value.trim().length < 20) {
                errors.push("Please write a message of at least 20 characters.");
            }

            if (errors.length) {
                event.preventDefault();
                alert(errors.join("\n"));
            }
        });
    }
});
