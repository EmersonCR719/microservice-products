import { createRouter, createWebHistory } from 'vue-router'
import HomeComponent from '../components/HomeComponent.vue';
import CrearProductoComponent from '../components/CrearProductoComponent.vue';
import ListarProductosComponent from '../components/ListarProductosComponent.vue';
import EliminarProducto from '../components/EliminarProducto.vue'
import ActualizarProducto from '../components/ActualizarProducto.vue';

const routes = [
  { path: '/', component: HomeComponent },
  { path: '/crear', component: CrearProductoComponent },
  { path: '/listar', component: ListarProductosComponent },
  { path: '/eliminar', component: EliminarProducto},
  { path: '/actualizar', component: ActualizarProducto},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
