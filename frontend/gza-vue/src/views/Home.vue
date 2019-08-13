<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <Geneza msg="Welcome to Your Vue.js App" />
  </div>
</template>

<script>
// @ is an alias to /src
import Geneza from "@/components/Geneza.vue";

export default {
  name: "home",
  components: {
    Geneza
  }
};
</script>
