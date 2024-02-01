document.addEventListener("DOMContentLoaded", () => {
  let isLateralNavAnimating = false;
  const navTrigger = document.querySelector(".cd-nav-trigger");
  navTrigger.addEventListener("click", (e) => {
    e.preventDefault();
    if (!isLateralNavAnimating) {
      if (navTrigger.closest(".csstransitions")) isLateralNavAnimating = true;
      document.body.classList.toggle("navigation-is-open");
      const navigationWrapper = document.querySelector(".cd-navigation-wrapper");
      navigationWrapper.addEventListener("webkitTransitionEnd",() => {isLateralNavAnimating = false;},{ once: true });
      navigationWrapper.addEventListener("otransitionend",() => {isLateralNavAnimating = false;},{ once: true });
      navigationWrapper.addEventListener("oTransitionEnd",() => {isLateralNavAnimating = false;},{ once: true });
      navigationWrapper.addEventListener("msTransitionEnd",() => {isLateralNavAnimating = false;},{ once: true });
      navigationWrapper.addEventListener("transitionend",() => {isLateralNavAnimating = false;},{ once: true });
    }
  });
});

const angle = 20;
const rotateCard = window;

const lerp = (start, end, amount) => {
  return (1 - amount) * start + amount * end;
};

const remap = (value, oldMax, newMax) => {
  const newValue = ((value + oldMax) * (newMax * 2)) / (oldMax * 2) - newMax;
  return Math.min(Math.max(newValue, -newMax), newMax);
};

window.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");
  cards.forEach((e) => {
    e.addEventListener("mousemove", (event) => {
      const rect = e.getBoundingClientRect();
      const centerX = (rect.left + rect.right) / 2;
      const centerY = (rect.top + rect.bottom) / 2;
      const posX = event.pageX - centerX;
      const posY = event.pageY - centerY;
      const x = remap(posX, rect.width / 2, angle);
      const y = remap(posY, rect.height / 2, angle);
      e.dataset.rotateX = x;
      e.dataset.rotateY = -y;
    });

    e.addEventListener("mouseout", () => {
      e.dataset.rotateX = 0;
      e.dataset.rotateY = 0;
    });
  });

  const update = () => {
    cards.forEach((e) => {
      let currentX = parseFloat(
        e.style.getPropertyValue("--rotateY").slice(0, -1)
      );
      let currentY = parseFloat(
        e.style.getPropertyValue("--rotateX").slice(0, -1)
      );
      if (isNaN(currentX)) currentX = 0;
      if (isNaN(currentY)) currentY = 0;
      const x = lerp(currentX, e.dataset.rotateX, 0.05);
      const y = lerp(currentY, e.dataset.rotateY, 0.05);
      e.style.setProperty("--rotateY", x + "deg");
      e.style.setProperty("--rotateX", y + "deg");
    });
  };
  setInterval(update, 1000 / 60);
});
