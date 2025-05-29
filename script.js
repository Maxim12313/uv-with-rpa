export function attach_listener() {
  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form");
    form.addEventListener(function (event) {
      event.preventDefault();
      const form_Data = new FormData(form);
      fetch(form.action, {
        method: "POST",
        body: form_data,
      });
    });
  });
}
