<template>
	<b-card @click="$emit('change-filter',type.id)" :img-src="type.src" :img-alt="type.name" img-top 
		class=" center border-0 " >
		<b-card-text class="text-align-center">
			{{type.name}}
		</b-card-text>
	</b-card>
</template>
<script>
export default {
	name:'Box',
	props:{
		type:Object,
	},
	emits:['change-filter'],
}
</script>