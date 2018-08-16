<template>
  <div>
      <b-form-group
          label="Choose risk form:"
          label-for="riskSelect">
          <b-form-select id="riskSelect"
              :options="this.risksList"
              required
              v-on:change="getForm">
          </b-form-select>
      </b-form-group>
      <b-form
          @submit="onSubmit"
          @reset="onReset"
          v-if="(this.riskFields).length > 0 ? true : false">
          <div v-for="(item, index) in this.riskFields" :key='index'>
              <Input
                  v-bind:key="item.id"
                  :item="item"
                  v-on:change_value="update"
              />
          </div>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
  </div>
</template>

<script>
import Input from "./Input.vue";

export default {
  name: "RiskForm",
  props: {
    risksList: Array,
    riskFields: Array
  },
  components: {
    Input
  },
  data() {
    return {
      formData: {}
    };
  },
  methods: {
    getForm(value) {
      /* Runs function to get get form schema on parent container component */
      this.$emit("getFormFields", value);
    },
    onSubmit(evt) {
      /* Submit placeholder */
      evt.preventDefault();
      alert(JSON.stringify(this.formData));
    },
    onReset(evt) {
      this.formData = {};
      evt.target.reset();
    },
    update(value, key) {
      /* Update form values */
      this.formData[key] = value;
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
