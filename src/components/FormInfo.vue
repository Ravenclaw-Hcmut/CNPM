<template>
    <div class="modall-backdrop">
        <div class="modall">
            <b-container>
                <h2>Customer Information</h2>
                <section class="form">
                    <div class="field">
                        <label class="label">Name</label>
                        <div class="control">
                            <input v-model="form.name" class="input" type="text" placeholder="Text input">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Address</label>
                        <div class="control">
                            <input v-model="form.address" class="input" type="text" placeholder="Text input">
                        </div>
                    </div>
                    <div class="field">
                        <label class="label">Phone Number</label>
                        <div class="control">
                            <input v-model="form.phone" class="input" type="text" placeholder="Text input">
                        </div>
                    </div>
                </section>
            </b-container>
        </div>
    </div>
</template>
<script>
export default {
    name:'FormInfo',
    data: {
        form :{
            name: '',
            address: '',
            phone: ''
        }
    }    
}
</script>

<style scope>
.modall-backdrop {
    position: fixed;
    top: 0;
	bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.5)!important;
    display: flex;
    justify-content: center;
    align-items: center;
	z-index: 50rem;
}
.modall {
	opacity: 1;
    background: rgba(256,256,256,255);
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
	width: 50rem;
	z-index: 100rem;
	border-radius:1rem ;
}  
</style>