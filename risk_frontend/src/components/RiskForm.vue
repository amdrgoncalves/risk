<template>
  <div>
    {{this.riskFields === []}}
    <b-form-group label="Choose risk form:"
                  label-for="riskSelect">
      <b-form-select id="riskSelect"
                    :options="this.risksList"
                    required
                    v-on:change="getForm">
      </b-form-select>
    </b-form-group>
    </b-form-select>
    <b-form @submit="onSubmit" @reset="onReset" v-if="(this.riskFields).length > 0 ? true : false">
      <div v-for="item in this.riskFields">
        <Input
          :key="item.id"
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
import Input from "./Input.vue"

var imported_list = [
    {
        "id": 1,
        "name": "Automobile"
    },
    {
        "id": 2,
        "name": "House"
    },
    {
        "id": 3,
        "name": "Prize"
    }
]

var options = imported_list.map((obj)=>(obj.name))



var imported_data = [
    {
        "id": 1,
        "type": "TEXT",
        "caption": "Driver Name",
        "options": null
    },
    {
        "id": 2,
        "type": "DATE",
        "caption": "Birth Date",
        "options": null
    },
    {
        "id": 3,
        "type": "NUM",
        "caption": "Car Year",
        "options": null
    },
    {
        "id": 4,
        "type": "ENUM",
        "caption": "Gender",
        "options": [
            "M",
            "F"
        ]
    }
]


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
      options: options,
      formData: {},
    };
  },
  methods: {
    getForm(value) {
      this.$emit('getFormFields',value);
    },
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.formData));
    },
    onReset(evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.formData = {}
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    update(value, key) {
      this.formData[key] = value;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
