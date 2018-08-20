import { shallowMount } from "@vue/test-utils";
import RiskForm from "@/components/RiskForm.vue";
 describe("RiskForm.vue", () => {
  it("renders correct items", () => {
    const riskFields = ['Automobile', 'House'];
    const wrapper = shallowMount(RiskForm, {
      propsData: { riskFields }
    });
    var expected = '<input-stub item="Automobile"></input-stub></div><div><input-stub item="House"></input-stub>'
    console.log(wrapper.html())
    expect(wrapper.html()).toContain(expected);
  });
});
