import formatError from "mysagw/utils/format-error";
import { module, test } from "qunit";

module("Unit | Utility | format-error", function () {
  test("it handles strings", function (assert) {
    const error = "Error";
    const result = formatError(error);
    assert.equal(result, "Error");
  });

  test("it handles normal errors", function (assert) {
    const error = new Error("Error");
    const result = formatError(error);
    assert.equal(result, "Error");
  });

  test("it handles JSON:API errors", function (assert) {
    const error = {
      errors: [{ detail: "Error 1" }, { detail: "Error 2" }],
    };
    const result = formatError(error);
    assert.equal(result, "Error 1, Error 2");
  });
});
