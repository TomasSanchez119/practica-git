  document.addEventListener('DOMContentLoaded', () => {
    const albumForm = document.getElementById('albumForm');
    const albumesContainer = document.getElementById('albumesContainer');

    let albumes = JSON.parse(localStorage.getItem('albumes')) || [];

    function renderAlbumes() {
      albumesContainer.innerHTML = '';
      albumes.forEach((album, index) => {
        const card = document.createElement('div');
        card.className = 'card shadow-sm';
        card.style.width = '18rem';

        card.innerHTML = `
          <div class="card-body text-center">
            <h5 class="card-title">${album.titulo}</h5>
            <h6 class="card-subtitle mb-2 text-muted">${album.anio} - ${album.medio}</h6>
            <p class="card-text">${album.descripcion}</p>
            <button class="btn btn-primary btn-sm me-2" onclick="modificar(${index})">Modificar</button>
            <button class="btn btn-danger btn-sm" onclick="borrar(${index})">Borrar</button>
          </div>
        `;

        albumesContainer.appendChild(card);
      });
    }

    albumForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nuevoAlbum = {
        titulo: document.getElementById('titulo').value,
        anio: document.getElementById('anio').value,
        medio: document.getElementById('medio').value,
        descripcion: document.getElementById('descripcion').value
      };

      albumes.push(nuevoAlbum);
      localStorage.setItem('albumes', JSON.stringify(albumes));
      renderAlbumes();
      albumForm.reset();
    });

    window.borrar = (index) => {
      if (confirm('¿Estás seguro de borrar este álbum?')) {
        albumes.splice(index, 1);
        localStorage.setItem('albumes', JSON.stringify(albumes));
        renderAlbumes();
      }
    };

    window.modificar = (index) => {
      const album = albumes[index];
      document.getElementById('titulo').value = album.titulo;
      document.getElementById('anio').value = album.anio;
      document.getElementById('medio').value = album.medio;
      document.getElementById('descripcion').value = album.descripcion;

      albumes.splice(index, 1); // se eliminará y se volverá a guardar al reenviar
      renderAlbumes();
    };

    renderAlbumes(); // inicializa
  });

