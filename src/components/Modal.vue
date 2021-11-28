<template>
  <div class="modall-backdrop">
    <div class="modall">
      <b-container class="mt-3 mb-3">
        <b-row>
          <b-col>
            <p class="float-left mx-2">Add to Cart</p>
            <b-button @click="$emit('close')" class="float-right mx-2">
              <b-icon icon="cart-x-fill"></b-icon>
            </b-button>
          </b-col>
        </b-row>
        <b-row>
          <b-col cols="4">
            <!-- <img src="" alt=""> -->
            <img
              :src="food.img"
              :alt="food.name"
              style="width: 100%; height: auto"
            />
            <!-- <img :src="food.src" :alt="food.name"> -->
          </b-col>
          <b-col>
            <b-container>
              <b-row class="mt-4">
                <b-col class="">
                  <div class="h2">{{ food.name }}</div>
                </b-col>
                <b-col>
                  <!-- <span class="buttonclass"><GooglePay /></span> -->
                  <span class="float-right mx-2 mt-0">
                    <span class="h2"> Price: {{ food.price }}</span>
                  </span>
                </b-col>
              </b-row>
              <b-row class="mt-4" style="margin-top: 0px">
                <b-col style="margin-top: 0px">
                  <h3>Quantity:</h3>
                </b-col>
                <b-col class="h3">
                  <span class="float-right">
                    <b-button size="sm" @click="subtract" variant="primary">
                      <b-icon icon="file-minus" aria-hidden="true"> </b-icon>
                    </b-button>
                    {{ food.qtity }}
                    <b-button size="sm" @click="add" variant="primary">
                      <b-icon icon="file-plus" aria-hidden="true"></b-icon>
                    </b-button>
                  </span>
                </b-col>
              </b-row>
              <b-row class="mt-4" style="margin-top: 0px">
                <b-col>
                  <h3>Select side dish &nbsp;</h3>
                  <span
                    v-for="name in Object.keys(this.food.side)"
                    :key="`${name}`"
                    class="mt-2"
                  >
                    <input
                      type="checkbox"
                      :id="name"
                      :value="side[name].name"
                      v-model="food.side[name]"
                    />
                    &nbsp;
                    <label :for="name">{{ side[name].name }} </label>
                    &nbsp;
                  </span>
                </b-col>
              </b-row>
              <b-row class="mt-4">
                <b-col>
                  <b-card-footer>
                    <b-button @click="OrderFood" class="float-right mx-2">
                      <b-icon icon="cart-check-fill"></b-icon>
                    </b-button>
                    <b-button @click="removeFood" class="float-left mx-2">
                      <b-icon icon="arrow-counterclockwise"></b-icon>
                    </b-button>
                  </b-card-footer>
                </b-col>
              </b-row>
            </b-container>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<script>
// import GooglePay from "./GooglePay";

export default {
  name: "ModalFood",
  props: {
    food: Object,
    side: Array,
  },
  components: {
    // GooglePay,
  },
  data() {
    return {
      selected: [],
    };
  },
  methods: {
    OrderFood() {
      this.selected.forEach((id) => (this.food.side[id] = true));
      this.$emit("order-up", this.food);
      alert("Added");
    },
    add() {
      if (this.food.qtity < 100) this.food.qtity++;
    },
    subtract() {
      if (this.food.qtity > 0) this.food.qtity--;
    },
    removeFood() {
      this.food.qtity = 0;
      // this.OrderFood() old
      this.selected.forEach((id) => (this.food.side[id] = true));
      this.$emit("order-up", this.food);
      alert("Reseted");
    },
  },
  emits: ["order-up", "close"],
};
</script>
<style scope>
.modall-backdrop {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background-color: rgba(0, 0, 0, 0.5) !important;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 50rem;
}

.modall {
  opacity: 1;
  background: rgba(256, 256, 256, 255);
  box-shadow: 2px 2px 20px 1px;
  overflow-x: auto;
  display: flex;
  flex-direction: column;
  width: 50rem;
  z-index: 100rem;
  border-radius: 1rem;
}
/* .buttonclass {
    text-align: center;
  } */
</style>
