<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
      <TextInput
        label="Text example"
        v-on:change_value="updateText"
      />
      <NumInput
        label="Number example"
        v-on:change_value="updateNum"
      />
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

var init_form = {}
imported_data.map((obj)=>{
  console.log(obj)
  init_form[obj.caption] = null
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
    return {
      form: {
        num: "",
        text: "",
        food: null,
        checked: []
      },

      foods: [
        { text: "Select One", value: null },
        "Carrots", "Beans", "Tomatoes", "Corn"
      ],
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      alert(JSON.stringify(this.form));
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
    updateText(value){
      this.form.text = value;
    },
    updateNum(value){
      this.form.num = value;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
