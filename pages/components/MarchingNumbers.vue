<template>
  <div class="numbers-grid" @click="increment">
    <slot name="zero">
      <div class="numbers-play"
        role="button"
        aria-pressed="false"
        aria-label="Play"
        >▶️</div>
    </slot>
    <div class="numbers-cell" v-for="index in count">{{ index }}</div>
  </div>
</template>


<script setup lang="ts">
import { ref, defineProps } from 'vue'

const {
  limit = 1000,
  factors = "3,5",
  delay_millis = 500,
} = defineProps<{
  limit?: number;
  factors: string;
  inert?: boolean;
  delay_millis: number;
}>()

const count = ref(1)
const v = factors.split(",").map((x) => Number(x))

const increment = () => {
  count.value++
  if (count.value < limit) {
    setTimeout(increment, delay_millis)
  }
}
</script>


<style lang="css"
 scoped>

.numbers-grid {
  display: grid;
  grid-template-columns: repeat(13, 2.2em);
  grid-gap: 5px;
}
.numbers-grid {
  width: 2.2em;
  line-height: 2.2em;
}

.numbers-play {
  border-radius: 5px;
  background-color: transparent;
  font-size: 2.2rem;
  line-height: 1em;
  width: 1em;
  text-align: left;
  position: relative; left: -.2em;
  user-select: none;
}
.numbers-play:hover {
  filter: brightness(120%);
  text-shadow: 1px 1px darkgray;
  cursor: pointer;
}

.numbers-play:active {
  filter: brightness(120%);
  cursor: grab;
}
</style>