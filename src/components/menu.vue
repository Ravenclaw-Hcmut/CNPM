<template>
  <div>
    <NavBar :Types="Types" @change-filter="PushChange" />

    <Store :Filter="Filt" :List="FoodList" @openmodal="OpenModal" />
  </div>
</template>
<script>
import NavBar from "./NavBar.vue";
import Store from "./Store.vue";

export default {
  name: "Menu",
  components: {
    NavBar,
    Store,
  },
  props: {
    Types: Array,
    FoodList: Array,
    Filt: Number,
  },
  methods: {
    PushChange(id) {
      const result = this.Types.find((type) => {
        return type.id === id;
      }).id;
      this.$emit("change-filter", result);
    },
    OpenModal(food) {
      this.$emit("openmodal", food);
    },
  },
  emits: ["change-filter", "openmodal"],
};
</script>
