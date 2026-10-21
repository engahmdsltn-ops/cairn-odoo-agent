import pytest

from build_site import BuildError, render

TPL = '<a href="{{REPO_URL}}">g</a> {{AUTHOR_NAME}} <a href="{{PORTFOLIO_URL}}">p</a>'


def cfg(name="Ada", portfolio="https://example.com/p", url="https://github.com/u/r"):
    return {"author": {"name": name, "portfolio_url": portfolio}, "repo": {"url": url}}


def test_fills_all_placeholders():
    out = render(TPL, cfg())
    assert "{{" not in out
    assert "https://github.com/u/r" in out and "Ada" in out


def test_escapes_values():
    out = render(TPL, cfg(name='<b>"x"</b>'))
    assert "<b>" not in out and "&lt;b&gt;" in out


def test_empty_name_fails():
    with pytest.raises(BuildError):
        render(TPL, cfg(name="  "))


@pytest.mark.parametrize("bad", ["http://example.com", "javascript:alert(1)", ""])
def test_non_https_portfolio_fails(bad):
    with pytest.raises(BuildError):
        render(TPL, cfg(portfolio=bad))


def test_non_https_repo_fails():
    with pytest.raises(BuildError):
        render(TPL, cfg(url="http://github.com/u/r"))


def test_leftover_placeholder_fails():
    with pytest.raises(BuildError):
        render(TPL + " {{OTHER}}", cfg())
