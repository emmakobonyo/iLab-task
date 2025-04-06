<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">IoT Gateway IP Display</h1>
    <button @click="connectToBroker" class="bg-blue-600 text-white px-4 py-2 rounded">
      Get IP Address
    </button>
    <p class="mt-4 text-lg">Received IP: <span class="font-mono">{{ ipAddress }}</span></p>
  </div>
</template>

<script setup>
import mqtt from "mqtt";
import { ref } from "vue";

const ipAddress = ref("Not received");
let client;

function connectToBroker() {
  client = mqtt.connect("ws://broker.emqx.io:8083/mqtt");

  client.on("connect", () => {
    console.log("Connected to MQTT broker");
    client.subscribe("iot/ip_address", (err) => {
      if (!err) console.log("Subscribed to topic");
    });
  });

  client.on("message", (topic, message) => {
    ipAddress.value = message.toString();
  });
}
</script>
