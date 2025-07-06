    import {getId} from "./file.js";
    import {username} from "./file.js"
    const text = getId("text");
    const inp = getId("inp");
    inp.addEventListener("input",(event) => {
      text.innerHTML = inp.value + username
    })
    document.addEventListener('DOMContentLoaded', function () {
      const loader = document.getElementById('loader');
      const allLinks = document.querySelectorAll('a');

      allLinks.forEach(link => {
        link.addEventListener('click', function () {
          loader.style.display = 'flex';
        });
      });
    });

