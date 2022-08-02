document.addEventListener("DOMContentLoaded", function (e) {
  async function get_cupcakes() {
    let response = await axios.get("/api/cupcakes");

    for (let cupcake of response.data.cupcakes) {
      let newCupcake = $(cupcakeHTML(cupcake));
      $("#cupcake-list").append(newCupcake);
    }
  }

  // Initate page with get request to API and display cupcake list
  $(get_cupcakes);

  function cupcakeHTML(cupcake) {
    // grab response values and pass into html created thru jquery
    return `
  <div class = "cupcake-div" data-id = "${cupcake.id}" id= ${cupcake.id}>
  <li> ${cupcake.flavor} cupcake | Size Available: ${cupcake.size}. | Rating: ${cupcake.rating}
  <img src = "${cupcake.image_url} "class = "image" alt= "cupcake-image">
  <button data-id= "${cupcake.id}" class = "del-button" > Delete </button> 
  </div>
  `;
  }

  async function delete_cupcake(e) {
    e.preventDefault();
    console.log("delete button was clicked");
    // reference Button = 'this' bc it was the element clicked on initiating the event function
    let id = $(this).data("id");
    let div = $(this).closest("div");

    // make API request to delete route
    let response = await axios.delete(`/api/cupcakes/${id}`);

    div.remove();
  }

  $("#cupcake-list").on("click", ".del-button", delete_cupcake);

  // Add cupcake upon form submission

  $("#cupcake-form").on("submit", async function (e) {
    e.preventDefault();
    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image_url = $("#image_url").val();

    // make api request passing in user input
    let response = await axios.post("/api/cupcakes", {
      flavor,
      size,
      rating,
      image_url,
    });

    // create the markup with response data for cupcake
    let newCupcake = $(cupcakeHTML(response.data.cupcake));
    $("#cupcake-list").append(newCupcake);
    $("#cupcake-form").trigger("reset");
  });
});
