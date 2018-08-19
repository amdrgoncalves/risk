<template>
  <div>
    <b-form-group v-bind:label="item.caption">
      <b-form-input
        v-if="item.type == 'TEXT'"
        type="text"
        v-on:input="update"
        required>
      </b-form-input>
      <b-form-input
        v-else-if="item.type == 'NUM'"
        type="number"
        v-on:input="update"
        required>
      </b-form-input>
      <b-form-select
        v-else-if="item.type == 'ENUM'"
        :options="optionPlusBlank"
        v-on:change="update"
        required>
      </b-form-select>
      <b-form-input
        v-else-if="item.type == 'DATE'"
        type="date"
        v-on:input="update"
        required>
      </b-form-input>
    </b-form-group>
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    item: Object
  },
  computed: {
    optionPlusBlank: function() {
      /* Adds blank option in the beginning */
      var options = this.item.options;
      options.unshift("");
      return options;
    }
  },
  methods: {
    /* update form variable on parent component */
    update(value) {
      this.$emit("change_value", value, this.item.id);
    }
  }
};
</script>
