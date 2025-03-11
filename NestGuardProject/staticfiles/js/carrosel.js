document.addEventListener("DOMContentLoaded", () => {
    const slides = document.querySelectorAll(".carousel-item");
    const indicators = document.querySelectorAll(".indicator");
    let currentIndex = 0;
  
    function updateCarousel() {
      // Atualizar o carrossel
      const offset = -currentIndex * 100;
      document.querySelector(".carousel-content").style.transform = `translateX(${offset}%)`;
  
      // Atualizar os indicadores
      indicators.forEach((indicator, index) => {
        indicator.classList.toggle("active", index === currentIndex);
      });
    }
  
    function nextSlide() {
      currentIndex = (currentIndex + 1) % slides.length;
      updateCarousel();
    }
  
    // Trocar slides a cada 5 segundos
    setInterval(nextSlide, 7000);
  
    // Adicionar eventos aos indicadores
    indicators.forEach((indicator, index) => {
      indicator.addEventListener("click", () => {
        currentIndex = index;
        updateCarousel();
      });
    });
  });
  