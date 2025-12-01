{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python314

    (python314.withPackages (p: with p; [
      requests
    ]))
  ];
}