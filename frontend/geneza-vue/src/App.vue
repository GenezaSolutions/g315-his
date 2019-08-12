<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Geneza msg="Welcome to Your Geneza App"/>
  </div>
</template>

<script>
import Geneza from './components/Geneza.vue'

export default {
  name: 'app',
  components: {
    Geneza
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
