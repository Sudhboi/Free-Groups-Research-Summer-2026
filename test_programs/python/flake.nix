{
  description = "Graph Tool Test";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      pkgs = nixpkgs.legacyPackages."x86_64-linux";
    in
    {
      devShells."x86_64-linux".default = pkgs.mkShell {
        buildInputs = with pkgs; [
          (python3.withPackages (
            ps: with ps; [
              graph-tool
              jupyter
              jupyterlab-vim
              jupyterlab-lsp
              numpy
              python-lsp-server
            ]
          ))
          python3
          basedpyright
          cairo
        ];
      };
    };
}
