<template>
  <div>
    <b-form-group v-bind:label="label"
                  label-for="exampleInput2">
      <b-form-input id="exampleInput2"
                    type="text"
                    v-on:input="update"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: "TextInput",
  props:{
    label: String,
    id: String
  },
  methods: {
    update: function (value) {
      this.$emit('change_value',value,this.id)
    }
  }
};
</script>
