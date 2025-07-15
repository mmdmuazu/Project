callback: function(response) {
  const cart = JSON.parse(localStorage.getItem("cart"));
  const total = cart.reduce((sum, item) => sum + item.price, 0);

  fetch("/save-order/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": "{{ csrf_token }}"
    },
    body: JSON.stringify({
      name: "Customer Name",  // replace with dynamic user if logged in
      email: "customer@email.com",
      items: cart,
      total: total,
      reference: response.reference
    }),
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === "success") {
      localStorage.removeItem("cart");
      window.location.href = "/thank-you/";
    }
  });
}
