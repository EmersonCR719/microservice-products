<template>
    <div class="container text-center mt-5">
      <h1>Página central</h1>
      <div class="mt-4">
        <router-link to="/crear" class="btn btn-primary mx-2">Crear Producto</router-link>
        <router-link to="/listar" class="btn btn-primary mx-2">Listar Productos</router-link>
        <router-link to="/eliminar" class="btn btn-primary mx-2">Eliminar Producto</router-link>
        <router-link to="/actualizar" class="btn btn-primary mx-2">Actualizar Producto</router-link>
      </div>
    </div>
  </template>
  
  <script setup>
  // No necesitamos lógica especial en este componente
  </script>
  
  <style scoped></style>