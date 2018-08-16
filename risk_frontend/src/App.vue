<template>
  <div id="app">
    <div>Risk form</div>

    <RiskFormContainer/>
  </div>
</template>

<script>
import RiskFormContainer from "./components/RiskFormContainer.vue";

export default {
  name: "app",
  components: {
    RiskFormContainer
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
