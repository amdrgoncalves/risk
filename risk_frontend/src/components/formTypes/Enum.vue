<template>
  <b-form-group id="exampleInputGroup3"
                label="Food:"
                label-for="exampleInput3">
    <b-form-select id="exampleInput3"
                  :options="foods"
                  required
                  v-model="form.food">
    </b-form-select>
  </b-form-group>
</template>

<script>
export default {
  name: "Enum",

  data () {
    return {
      foods: [
        { text: 'Select One', value: null },
        'Carrots', 'Beans', 'Tomatoes', 'Corn'
      ]
    }
  }
};
</script>
