<script setup>

import { ref } from 'vue';

const props = defineProps({
    card: {
        type: String,
        required: true
    },
    cardImage: {
        type: String,
        required: true
    }
});

const isSelected = ref(false)

function toggleSelect() {
    isSelected.value = !isSelected.value;
}

</script>

<template>
    <div class="card" :class="{'selected': isSelected}" @click="toggleSelect">
        <img :src="cardImage">
    </div>
</template>

<style scoped>

.card {
    display: inline-block;
    width: 100%;
    height: 100%;
    margin: 10px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}


.card.selected {
    transform: translateY(-10px);
    box-shadow:  0px 4px 10px rgba(0, 0, 0, 0.2);
}

.card img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

</style>

