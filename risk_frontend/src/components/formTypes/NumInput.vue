<template>
  <div>
    <b-form-group id="exampleInputGroup2"
                  v-bind:label="label"
                  label-for="exampleInput2">
      <b-form-input id="exampleInput2"
                    type="number"
                    v-on:input="update"
                    required
                    placeholder="Enter number">
      </b-form-input>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: "NumInput",
  props: {
    label: String,
  },
  methods: {
    update: function (value) {
      this.$emit('change_value',value)
    }
  }
};
</script>
