
export const onRequest = async (context) => {
  //const value = await context.env.KV.get("example");

  return new Response("the time is " + (new Date()).toISOString());
};