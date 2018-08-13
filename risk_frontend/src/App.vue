<template>
  <div id="app">
    <div>Risk form</div>

    <RiskForm msg='Alex'/> 
  </div>
</template>

<script>
import RiskForm from "./components/RiskForm.vue";

export default {
  name: "app",
  components: {
    RiskForm
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
