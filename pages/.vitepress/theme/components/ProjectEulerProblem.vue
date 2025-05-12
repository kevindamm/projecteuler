<template>
  <div>
    <slot name="default"></slot>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  n: number
}>();
</script>
