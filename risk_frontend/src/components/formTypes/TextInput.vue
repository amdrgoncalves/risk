<template>
  <div>
    <b-form-group id="exampleInputGroup2"
                  v-bind:label="label"
                  label-for="exampleInput2">
      <b-form-input id="exampleInput2"
                    type="text"
                    v-on:input="updateText"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: "TextInput",
  props: {
    label: String,
  },
  methods: {
    updateText: function (value) {
      this.$emit('change_value',value)
    }
  }
};
</script>
