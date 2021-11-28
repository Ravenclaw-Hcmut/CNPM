<template>
  <div class="modall-backdrop">
    <div class="modall">
      <b-container class="mt-3 mb-3">
        <b-row>
          <b-col>
            <b-button @click="$emit('close')" class="float-right mx-2">
              <b-icon icon="x-circle"></b-icon>
            </b-button>
          </b-col>
        </b-row>
        <b-row>
          <div><span>Name</span></div>
          <input type="text" v-model="name" />
        </b-row>
        <b-row>
          <div><span>Address</span></div>
          <div>
            <input type="text" v-model="address" />
          </div>
        </b-row>
        <b-row>
          <div><span>Phone number</span></div>
          <div>
            <input type="text" v-model="phone_number" />
          </div>
        </b-row>
        <b-row>
          <p>Total price: {{ pay_total }}$</p>
        </b-row>
        <b-row>
          <button @click="sendOrder">Xác nhận</button>
        </b-row>
      </b-container>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    pay_total: String,
  },
  data() {
    return {
      name: "",
      address: "",
      phone_number: "",
    };
  },
  methods: {
    sendOrder() {
      axios
        .post("http://localhost:8000/api/foodorders/", {
          price: this.pay_total,
          name: this.name,
          address: this.address,
          phone_number: this.phone_number,
          food: [],
        })
        .then((respone) => console.log(respone))
        .catch((err) => alert(err));
        
      this.name = this.address = this.phone_number = '';
      this.$emit('close');
    },
  },
};
</script>