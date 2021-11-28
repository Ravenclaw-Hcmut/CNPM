<template>
  <div>
    <div>
      <b-button @click="togglePayment = true">Điền thông tin thanh toán</b-button>
    </div>
    <modal-payment :pay_total="pay_total" @close="closePayment" v-show="togglePayment"/>
  </div>
</template>

<script lang="js">
import ModalPayment from './ModalPayment.vue';

export default {
  props: {
    pay_total: String
  },
  components: {
    'modal-payment': ModalPayment,
  },
  data() {
    return {
      togglePayment: false,
    }
  },
  methods: {
    closePayment() {
      this.togglePayment = false;
    },
  }
}
</script>