<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <!-- reference from https://jsfiddle.net/Herteby/utkhb79n/ -->
      <div v-for="item, key in schema">
        <TextInput
          v-if="item.type == 'text' && item.options != null"
          :id="key"
          v-bind:label="item.caption"
          v-on:change_value="update"
        />
        <TextInput
          v-else-if="item.type == 'text'"
          :id="key"
          v-bind:label="item.caption"
          v-on:change_value="update"
        />
        <NumInput
          v-else-if="item.type == 'number'"
          :id="key"
          v-bind:label="item.caption"
          v-on:change_value="update"
        />


      </div>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
import TextInput from "./formTypes/TextInput.vue"
import NumInput from "./formTypes/NumInput.vue"

var imported_data = [
  {
      "type": "TEXT",
      "caption": "Name",
      "options": null
  },
  {
      "type": "DATE",
      "caption": "BirthDate",
      "options": null
  },
  {
      "type": "NUM",
      "caption": "Age",
      "options": null
  },
  {
      "type": "ENUM",
      "caption": "Gender",
      "options": [
          "M",
          "F"
      ]
  }
]

// Calculates initial from
var schema = {}
imported_data.map((obj,index)=>{
  console.log(obj)
  if(obj.type=="TEXT"){
    schema[index.toString()] = {
      type: "text",
      caption: obj.caption
    }
  }else if(obj.type=="NUM"){
    schema[index.toString()] = {
      type: "number",
      caption: obj.caption
    }
  }else if(obj.type=="ENUM"){
    schema[index.toString()] = {
      type: "text",
      caption: obj.caption
    }
  }else if(obj.type=="DATE"){
    schema[index.toString()] = {
      type: "date",
      caption: obj.caption
    }
  }
})



export default {
  name: "RiskForm",
  props: {
    msg: String
  },
  components:{
    TextInput,
    NumInput
  },
  data () {
    console.log(schema)

    return {

      schema: schema,
      formData: {},
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.formData));
    },
    onReset(evt) {
      evt.preventDefault();
      /* Reset our form values */
      this.form.num = "";
      this.form.text = "";
      this.form.food = null;
      this.form.checked = [];
      /* Trick to reset/clear native browser form validation state */
      this.show = false;
      this.$nextTick(() => {
        this.show = true
      });
    },
    update(value,key){
      this.formData[key] = value;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
