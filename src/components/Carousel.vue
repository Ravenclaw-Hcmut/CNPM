<template>

    <div>
        <!-- carousel area -->
        <b-card-group deck class="mb-0">
            <b-card
                v-for="item in currentPageCards"
                :key="item.index"
                class="center border-2"
                @click="$emit('change-filter',item.id)" :img-src="item.src" :img-alt="item.name" img-top>
            >
                <!-- card content -->
                <b-card-text class="text-align-center">{{ item.name }}</b-card-text>
            </b-card>
        </b-card-group>


        <!-- pagination area -->
        <div class="pagination" :v-if="cards.length > cardsPerPage">
            <div
                class="index"
                v-for="i in pageCount"
                :key="i"
                @click="next(i)"
                :class="{ active: currentPage(i) }"
            ></div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Carousel',
    data() {
        return {
            cards: this.Types,
            paginatedCards: [],
            pageCount: 0,
            cardsPerPage: 5,
            currentPageIndex: 0
        }
    },
    created() {
        this.cards = this.Types;
        console.log(this.cards)
    },
    computed: {
        currentPageCards() {

            this.createPages();

            return this.paginatedCards[this.currentPageIndex];
        }
    },
    props: {
        Types: Array,
    },
    methods: {
        currentPage(i) {
            return i - 1 === this.currentPageIndex;
        },

        createPages() {
            let cardsLength = this.Types.length;
            console.log(cardsLength)
            let fullPagesCount = Math.floor(cardsLength / this.cardsPerPage);

            if (cardsLength > this.cardsPerPage) {
                this.pageCount = 0;
                for (let i = 0; i < fullPagesCount * this.cardsPerPage; i += this.cardsPerPage) {
                    this.paginatedCards[this.pageCount] = this.Types.slice(i, i + this.cardsPerPage);
                    this.pageCount++;
                }

                this.paginatedCards[this.pageCount] = this.Types.slice(cardsLength - this.cardsPerPage, cardsLength);
                this.pageCount = this.pageCount + 1;
            } else {
                this.paginatedCards[0] = this.Types;
            }
        },

        next(i) {
            this.currentPageIndex = i - 1;
        }
    },
    emits: ['change-filter'],
}
</script>
<style scoped>
.pagination {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
}

.index {
    margin-left: 10px;
    width: 10px;
    height: 10px;
    background: #000000;
}

.active {
    width: 2rem;
    height: 2rem;
}
</style>
