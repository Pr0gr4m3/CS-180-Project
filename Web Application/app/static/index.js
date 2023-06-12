async function handleSubmit(event) {
  event.preventDefault();

  const data = new FormData(event.target);

  const value = Object.fromEntries(data.entries());

  console.log({ value });

  try {
    const response = await fetch("/predict", {
      body: JSON.stringify(value),
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    });
    const output = document.querySelector("#response_col");
    const jsonData = await response.json();

    output.innerHTML = jsonData.sleep_efficiency;

  } catch (error) {
    console.error("Error:", error);
  }
}

const form = document.querySelector("form");
form.addEventListener("submit", handleSubmit);
