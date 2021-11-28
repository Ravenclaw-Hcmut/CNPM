<template>
  <div>
    <b-container fluid>
      <b-row>
        <b-col sm="8" cols="12">
          <Menu
            :Filt="getFilterId()"
            :FoodList="List"
            :Types="Types"
            @change-filter="changeFilter"
            @openmodal="getModal"
          />
        </b-col>
        <b-col sm="4" cols="12">
          <h1
            style="
              font-size: 55px;
              font-weight: lighter;
              border-bottom: solid 2px lightgrey;
            "
          >
            Your Cart
          </h1>
          <div
            class="header"
            style="
              display: flex;
              justify-content: space-between;
              background-color: #e8e8e8;
              border: solid 1px lightgray;
              padding-top: 10px;
            "
          >
            <p style="margin-left: 10px">Item</p>
            <p style="margin-right: 10px">Price</p>
          </div>
          <div
            v-for="food in Cart"
            :key="food.id"
            style="
              display: flex;
              justify-content: space-between;
              background-color: #e8e8e8;
              border-radius: 10px;
              margin: 20px auto;
            "
          >
            <h1
              v-if="food.qtity > 0"
              style="font-weight: lighter; font-size: 40px; margin-left: 10px"
            >
              {{ food.qtity }} x {{ food.name }}:
            </h1>
            <h1
              v-if="food.qtity > 0"
              style="text-align: right; margin-right: 10px; color: #fa5401"
            >
              ${{ food.price }}
            </h1>
          </div>
          <div
            style="
              text-align: right;
              font-size: 40px;
              border-top: double 2px lightgrey;
            "
          >
            Total: ${{ total }}
          </div>

          <div class="buttonclass">
            <GooglePay :pay_total="total" />
          </div>
        </b-col>
      </b-row>
    </b-container>
    <ModalFood
      :side="side"
      :food="food"
      @close="closeModal"
      v-show="this.openModal"
      @order-up="addFood"
    />
  </div>
</template>

<script lang="js">
import Menu from './components/menu.vue'
import ModalFood from './components/Modal.vue'
import GooglePay from "./components/GooglePay";
import axios from 'axios';


export default {
  name: 'App',
  components: {
    Menu, ModalFood,
    GooglePay,
  },
  data() {
    return {
      Types: [],
      List: [],
      filterID: 1,
      Cart: [],
      food: Object,
      openModal: Boolean,
      total: Number,
      side: [],
    }
  },
  // mounted() {

  // },
  created() {
    // this.List = [
    //   {
    //     id: 1, name: 'Coca', type: 5, price: 50, qtity: 0, img: 'https://lh3.googleusercontent.com/pw/AM-JKLWW2wgYdcV2RpAZOV8rByBDqg2UlRHETQoVwYRJG-qTbgkGL6yfnoqQ3pOrVEYHEKNN1oJtMcgm8K1fGZSoSI-SeY6pqjBsI7WdgkzKXPgy-V-ZsWcx5e7YT_SxDtTDmw93E33wTGs05hv93meZ48GG1A=w820-h512-no?authuser=1',
    //     side: { 'fried': false, 'salad': false, 'pop': false }
    //   },
    //   {
    //     id: 2, name: 'Apple juice', type: 4, price: 80, qtity: 0, img: 'https://lh3.googleusercontent.com/pw/AM-JKLXmzWP3nJwfmCOOEsoPyj02kdkzd_TSrZZReTh1s3Qi_1IsbMHSnWti6cpfD-BzhW43R-pPWx3_pcdw3htyeahRsMJtH67MOZtLsXEBLjpq5Dqj7vJqtkQlF42AzPOwQ5bxtPoNksStIud5oPQdnriBkA=w480-h538-no?authuser=1', //538
    //     side: { 'fried': false, 'salad': false, 'pop': false }
    //   },
    //   {
    //     id: 3, name: 'Cup cake', type: 3, price: 60, qtity: 0, img: 'https://lh3.googleusercontent.com/pw/AM-JKLUrXXhDhsYkm778c36IZ04qkN4zOJV3VwwgJHsnwOdv6O2tntrqNONuyEk6kDnEcRezVsNtF7BwWpiHWMmu8TRlKZ8wki2WEfSZrJaCMUEU-HX3CaUB9UOlJy6PKIJOCVUggovr-O8Hn09tY1VVpjcgMg=w840-h726-no?authuser=1',
    //     side: { 'fried': false, 'salad': false, 'pop': false }
    //   },
    //   {
    //     id: 4, name: 'Fish', type: 2, price: 100, qtity: 0, img: 'https://lh3.googleusercontent.com/pw/AM-JKLXinyrXF2AHnKoyLHiqacNgZJclVvH5NxHTJiJfJ0fkgxt-t8hwmcgEAQsX7jAd_rhVQjJ5NJqrJgVzfj0ZeH8_h5dhmBxTj0m62QBBh3ZMHGA6cAS-k23etGZvc1fUTxOtP8uc7JAe8hubMa4rhRLm7w=w920-h612-no?authuser=1',
    //     side: { 'fried': false, 'salad': false, 'pop': false }
    //   },
    //   {
    //     id: 5, name: 'Steake', type: 6, price: 90, qtity: 0, img: 'https://lh3.googleusercontent.com/pw/AM-JKLUa2ELcP3RyqxgmFzsd0cRsYMTHUC8GvTJvhOUoTXjJyLwijEiOpOypOxuQuLfzZgHynPBnby07GQ6Jxu_uuTlE2TBcQhC9doNr7dzhss0FNqIJOU-Pl08A8WoAlkL_6lmvEZCdyqSWq01zyJfpLgi_Bw=w900-h619-no?authuser=1',
    //     side: { 'fried': false, 'salad': false, 'pop': false }
    //   },
    // ]
    axios
      .get('http://localhost:8000/api/foods/')
      .then(respone => {
        this.List = respone.data;
      })
      .catch(err => alert(err))

    axios
      .get('http://localhost:8000/api/type/')
      .then(respone => {
        this.Types = respone.data;
      })
      .catch(err => alert(err))

    axios
      .get('http://localhost:8000/api/side/')
      .then(respone => {
        this.side = respone.data;
      })
      .catch(err => alert(err))

    this.Cart = []
    this.food = this.List[0]
    this.openModal = false;
    this.total = 0
  },
  methods: {
    changeFilter(id) {
      this.filterID = id
      // console.log(this.filter)
    },
    addFood(food) {
      const index = this.List.findIndex((x) => { return x.id === food.id })
      let newList = [...this.List]

      newList[index] = food
      this.List = [...newList]
      const index_nd = this.Cart.findIndex((type) => type.id === food.id)
      console.log(index_nd)
      if (index_nd < 0) {
        this.Cart = [...this.Cart, food]
      } else {
        this.Cart[index_nd] = food

      }
      // console.log(this.Cart)
      this.total = 0
      this.Cart.forEach(element => {
        this.total += element.price * element.qtity
      });
      let temp = this.Cart.filter((item) => item.qtity > 0)
      this.Cart = temp
      console.log(this.Cart)
    },
    closeModal() {
      this.openModal = false;
    },
    getModal(id) {
      const index = this.List.findIndex((food) => food.id === id)
      this.food = this.List[index]
      this.openModal = true
    },
    getFilterId() {
      return this.filterID;
    },
  }
}
</script>

<style>
.foodBox_class img {
  /* float: left; */
  /* width:  100px; */
  height: 250px;
  object-fit: cover;
}
.buttonclass {
  text-align: center;
}
</style>
