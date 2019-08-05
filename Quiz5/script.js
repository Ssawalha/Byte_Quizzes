const button = document.getElementById("search")
const output = document.getElementById("output")
const input = document.getElementById("pokemon")

let weight = null

function findWeight(event) {
    event.preventDefault()
    const promise = fetch(`https://pokeapi.co/api/v2/pokemon/${input.value}`)
    promise.then(response => response.json()).then(json=>{
        output.innerHTML = `${input.value} has a weight of ${json['weight']}.`
    })
}

button.addEventListener("click", findWeight)