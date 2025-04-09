const holaMundo = require("../index");

test("Debe devolver '¡Hola, Mundo!'", () => {
    expect(holaMundo()).toBe("¡Hola, Mundo!");
});