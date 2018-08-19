<template>
  <div class="narrow">
    <b-container>
      <RiskForm
        :risksList="risksList"
        :riskFields="riskFields"
        v-on:getFormFields="getFormFields"
      />
    </b-container>
  </div>
</template>

<script>
import axios from "axios";
import RiskForm from "./RiskForm.vue";

export default {
  name: "RiskFormContainer",
  methods: {
    getFormFields(key) {
      /* Find fields on API */
      this.risks.map(obj => {
        if (obj.name == key) {
          axios
            .get(
              "http://localhost:8000/api/v1/risks/" + obj.id.toString() + "/"
            )
            .then(response => {
              this.riskFields = response.data[0].risk_field;
            });
        }
      });
    }
  },
  components: {
    RiskForm
  },
  data() {
    return {
      risks: null,
      risksList: [],
      riskFields: []
    };
  },
  mounted() {
    axios.get("http://localhost:8000/api/v1/risks/").then(response => {
      this.risks = response.data;
      this.risksList = response.data.map(obj => obj.name);
    });
  }
};
</script>

<style scoped>
.narrow {
  margin-left: 30%;
  margin-right: 30%;
}
</style>
