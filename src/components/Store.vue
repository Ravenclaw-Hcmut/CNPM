<template>
  <b-container>
    <b-row class="justify-content-center">
      <b-col
        cols="12"
        sm="4"
        v-for="food in FoodList"
        :key="food.id"
        class="justify-content-center"
      >
        <FoodBox :food="food" @openmodal="OpenModal" />
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import FoodBox from "./Foodbox.vue";
export default {
  components: { FoodBox },
  name: "Store",
  props: {
    List: Array,
    Filter: Number,
  },
  data() {
    return {
      FoodList: this.List,
    };
  },
  watch: {
		List() {
			this.FoodList = this.List;
		},
    Filter() {
      if (this.Filter !== 1)
        this.FoodList = this.List.filter((food) => {
          return food.type.includes(this.Filter);
        });
      else this.FoodList = this.List;
    },
  },
  methods: {
    OpenModal(food) {
      this.$emit("openmodal", food);
    },
  },
  emits: ["openmodal"],
};
</script>
