with import <nixpkgs> {};

let
  libPath = lib.makeLibraryPath [
    openssl
  ];
in stdenv.mkDerivation {
  name = "steelconnect-dialogflow-env";

  buildInputs = (with python27Packages; [
    python
    pip
  ]) ++ [
    pkgconfig

    openssl
  ];

  PYTHONPATH = ".:" + (builtins.getEnv "HOME") + "/.local/lib/python2.7/site-packages/";

  shellHook = ''
    export LD_LIBRARY_PATH="${libPath}:$LD_LIBRARY_PATH"
  '';

  # Run `source installDeps`
  installDeps = ''
    pip install -U --user -r requirements-dev.txt
  '';
}
