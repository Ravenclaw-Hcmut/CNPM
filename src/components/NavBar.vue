<template>
	<div>
		<b-nav class="border justify-content-center">
			<b-nav-item>
				<Carousel :Types="Types" @change-filter="emitCarousel"/>
			</b-nav-item>
			
		</b-nav>
	</div>
</template>
<script>
//import Box from './Box.vue'
import Carousel from './Carousel.vue'

export default {
	name:'NavBar',
	components:{
		//Box,
Carousel,
	},
	props:{
		Types:Array
	},
	emits:['change-filter'],
	methods:{
		emitCarousel(id){
			this.$emit('change-filter',id)
		}
	},
}
</script>